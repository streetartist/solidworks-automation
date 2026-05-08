# SetBreakCorners Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~SetBreakCorners`

Sets whether to add break corners to the Flat-Pattern feature.
Sets whether to add break corners to the Flat-Pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetBreakCorners( _
   ByVal BBreakCorner As System.Boolean _
) 
```

```

Dim instance As IFlatPatternFeatureData
Dim BBreakCorner As System.Boolean
 
instance.SetBreakCorners(BBreakCorner)
```

```

void SetBreakCorners( 
   System.bool BBreakCorner
)
```

```

void SetBreakCorners( 
   System.bool BBreakCorner
) 
```

#### Parameters

*BBreakCorner*
:   True to add break corners, false to not

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.md)  
[IFlatPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.md)  
[IFlatPatternFeatureData::GetBreakCorners Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~GetBreakCorners.md)  
[IFlatPatternFeatureData::BreakCornerRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~BreakCornerRadius.md)  
[IFlatPatternFeatureData::BreakCornerType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~BreakCornerType.md)  
[IBreakCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData.md)
