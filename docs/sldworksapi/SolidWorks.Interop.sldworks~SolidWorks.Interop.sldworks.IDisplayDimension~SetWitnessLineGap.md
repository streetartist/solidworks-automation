# SetWitnessLineGap Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetWitnessLineGap`

Sets the gap for the specified dimension extension line.
Sets the gap for the specified dimension extension line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetWitnessLineGap( _
   ByVal WitnessIndex As System.Short, _
   ByVal UseDoc As System.Boolean, _
   ByVal Gap As System.Double _
) As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim WitnessIndex As System.Short
Dim UseDoc As System.Boolean
Dim Gap As System.Double
Dim value As System.Boolean
 
value = instance.SetWitnessLineGap(WitnessIndex, UseDoc, Gap)
```

```

System.bool SetWitnessLineGap( 
   System.short WitnessIndex,
   System.bool UseDoc,
   System.double Gap
)
```

```

System.bool SetWitnessLineGap( 
   System.short WitnessIndex,
   System.bool UseDoc,
   System.double Gap
) 
```

#### Parameters

*WitnessIndex*
:   Index of the extension line whose gap to get

*UseDoc*
:   True to use the document default value of the gap, false to not (see **Remarks**)

*Gap*
:   Gap value in system units; ignored if UseDoc is true

#### Return Value

True if the operation succeeds, false if not

Remarks

The UseDoc argument is dependent on the detailing standard. You can retrieve the document default value using the [document-level user-preference swDetailingWitnessLineGap](ms-help://SolidWorks.Interop.swconst/SolidWorks/DP_Dimensions.htm).

Call [IModelView::GraphicsRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GraphicsRedraw.md) after calling this method to redraw the graphics area.

Example

[Get and Set Dimension Extension Lines Gaps (VBA)](Get_and_Set_Dimension_Extension_Lines_Gaps_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::SetWitnessLineGap Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetWitnessLineGap.md)  
[IView::GetDimensionInfo6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionInfo6.md)  
[IView::IGetDimensionInfo6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionInfo6.md)
