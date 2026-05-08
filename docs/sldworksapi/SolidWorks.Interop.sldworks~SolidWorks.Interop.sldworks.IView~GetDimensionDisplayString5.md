# GetDimensionDisplayString5 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayString5`

Gets all of the dimension text in the current drawing sheet or the current drawing view.
Gets all of the dimension text in the current drawing sheet or the current drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDimensionDisplayString5( _
   ByRef DimensionSize As System.Integer _
) As System.Object
```

```

Dim instance As IView
Dim DimensionSize As System.Integer
Dim value As System.Object
 
value = instance.GetDimensionDisplayString5(DimensionSize)
```

```

System.object GetDimensionDisplayString5( 
   out System.int DimensionSize
)
```

```

System.Object^ GetDimensionDisplayString5( 
   [Out] System.int DimensionSize
) 
```

#### Parameters

*DimensionSize*
:   Number of strings for each dimension (see **Remarks**)

#### Return Value

Array of strings (see **Remarks**)

Remarks

This method returns a string array of size (*DimensionSize*) x (*number\_of\_dimensions\_in\_view*).

This set of values returned for each dimension in the view:

[ value1, tolMax1 tolMin1, value2, tolMax2, tolMin2, prefix, suffix, callout1, callout2, bottom ]

where:

> *value1* = Primary Dimension Value
>
> *tolMax1* = Maximum Variation for *value1*
>
> *tolMin1* = Minimum Variation for *value1*
>
> *value2* = Dual Dimension Value
>
> *tolMax2* = Maximum Variation for *value2*
>
> *tolMin2* = Minimum Variation for *value2*
>
> *prefix* = Text before *value1*
>
> *suffix* = Text after *value1*
>
> *callout1* = Text above *prefix*<*value1*>*suffix*
>
> *callout2* = Text below *prefix*<*value1*>*suffix*
>
> *bottom* = Text below *callout2*

The Dimension PropertyManager page (PMP) contains two Dimension Text boxes. Add dimension text by entering prefix, suffix, callout1, and callout2 texts in the first Dimension Text box. Enter bottom text in the second Dimension Text box.

If any of the above values are not used in the dimension, then those values are returned as empty strings in the returned array of this method.

For more information, see **SOLIDWORKS user-interface help > Detailing and Drawings > Drawings > Dimensions in Drawings > Dimension Value PropertyManager**.

NOTES:

- A previous version of this method, [IView::GetDimensionDisplayString2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayString2.md), detects and overlooks dangling dimensions. This method neither overlooks nor indicates that any dimensions are dangling. Use IView::GetDimensionDisplayString2 if you need dangling dimensions detected and overlooked.
- This method does not support [hole callouts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsHoleCallout.md).

Example

'VBA

' Open a drawing that has one or more display dimensions

'=============================================

Dim swApp As SldWorks.SldWorks

Dim swModel As ModelDoc2

Dim swDraw As DrawingDoc

Dim swView As View

Option Explicit

Sub main()

    Set swApp = Application.SldWorks

    Set swModel = swApp.**ActiveDoc**

   

    Set swDraw = swModel

   

    Dim views As Variant

    views = swDraw.**GetViews**()

   

    Set swView = views(0)(0)

    Dim var As Variant

    Dim size As Long

    var = swView.**GetDimensionDisplayString5**(size)

   

    Debug.Print "Number of strings in returned array: " & UBound(var) + 1

    Debug.Print "Number of strings for each display dimension: " & size

End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetDimensionDisplayInfo5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayInfo5.md)  
[IView::GetDimensionDisplayInfoSize2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionDisplayInfoSize2.md)  
[IView::GetDimensionIds4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionIds4.md)  
[IView::GetDimensionInfo7 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionInfo7.md)  
[IView::GetDimensionString4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionString4.md)  
[IView::GetFirstDisplayDimension5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDisplayDimension5.md)  
[IView::ProjectedDimensions Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ProjectedDimensions.md)
