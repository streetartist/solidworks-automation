# SetFarSideElements Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData~SetFarSideElements`

Sets the far side hole elements in this Advanced Hole.
Sets the far side hole elements in this Advanced Hole.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetFarSideElements( _
   ByVal ElmArray As System.Object _
) 
```

```

Dim instance As IAdvancedHoleFeatureData
Dim ElmArray As System.Object
 
instance.SetFarSideElements(ElmArray)
```

```

void SetFarSideElements( 
   System.object ElmArray
)
```

```

void SetFarSideElements( 
   System.Object^ ElmArray
) 
```

#### Parameters

*ElmArray*
:   Array of far side hole elements

Remarks

See [Accessing Selections that Define Features](sldworksapiprogguide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Example

See the [IAdvancedHoleFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAdvancedHoleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData.md)  
[IAdvancedHoleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData_members.md)  
[IAdvancedHoleFeatureData::GetFarSideElements Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData~GetFarSideElements.md)
