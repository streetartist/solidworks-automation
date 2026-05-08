# GetWitnessLineGap Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetWitnessLineGap`

Gets the gap of the specified dimension extension line.
Gets the gap of the specified dimension extension line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetWitnessLineGap( _
   ByVal WitnessIndex As System.Short, _
   ByRef UseDoc As System.Boolean, _
   ByRef Gap As System.Double _
) As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim WitnessIndex As System.Short
Dim UseDoc As System.Boolean
Dim Gap As System.Double
Dim value As System.Boolean
 
value = instance.GetWitnessLineGap(WitnessIndex, UseDoc, Gap)
```

```

System.bool GetWitnessLineGap( 
   System.short WitnessIndex,
   out System.bool UseDoc,
   out System.double Gap
)
```

```

System.bool GetWitnessLineGap( 
   System.short WitnessIndex,
   [Out] System.bool UseDoc,
   [Out] System.double Gap
) 
```

#### Parameters

*WitnessIndex*
:   Index of the extension line whose gap to get

*UseDoc*
:   True if using the document default value of the gap, false if not (see **Remarks**)

*Gap*
:   Gap value in system units (see **Remarks**)

#### Return Value

True if the operation succeeds, false if not

Remarks

The UseDoc argument is dependent on the detailing standard. You can retrieve the document default value using the [document-level user-preference swDetailingWitnessLineGap](ms-help://SolidWorks.Interop.swconst/SolidWorks/DP_Dimensions.htm).

The Gap argument is the document default value if UseDoc is true; otherwise, the value returned is the locally set value.

Example

[Get and Set Dimension Extension Lines Gap (VBA)](Get_and_Set_Dimension_Extension_Lines_Gaps_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::SetWitnessLineGap Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetWitnessLineGap.md)  
[IView::GetDimensionInfo6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDimensionInfo6.md)  
[IView::IGetDimensionInfo6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDimensionInfo6.md)
