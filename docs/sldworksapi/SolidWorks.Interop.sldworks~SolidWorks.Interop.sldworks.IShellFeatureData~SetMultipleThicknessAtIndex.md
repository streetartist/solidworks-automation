# SetMultipleThicknessAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~SetMultipleThicknessAtIndex`

Sets the thickness of the shell at this index in this shell feature.
Sets the thickness of the shell at this index in this shell feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetMultipleThicknessAtIndex( _
   ByVal Index As System.Integer, _
   ByVal Thickness As System.Double _
) 
```

```

Dim instance As IShellFeatureData
Dim Index As System.Integer
Dim Thickness As System.Double
 
instance.SetMultipleThicknessAtIndex(Index, Thickness)
```

```

void SetMultipleThicknessAtIndex( 
   System.int Index,
   System.double Thickness
)
```

```

void SetMultipleThicknessAtIndex( 
   System.int Index,
   System.double Thickness
) 
```

#### Parameters

*Index*
:   0-based index for new thickness

*Thickness*
:   New thickness

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IShellFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData.md)  
[IShellFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData_members.md)  
[IShellFeatureData::GetMultipleThicknessAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~GetMultipleThicknessAtIndex.md)  
[IShellFeatureData::GetMultipleThicknessFacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~GetMultipleThicknessFacesCount.md)  
[IShellFeatureData::ISetMultipleThicknessFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~ISetMultipleThicknessFaces.md)  
[IShellFeatureData::MultipleThicknessFaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~MultipleThicknessFaces.md)  
[IShellFeatureData::Thickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~Thickness.md)  
[IShellFeatureData::IGetMultipleThicknessFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~IGetMultipleThicknessFaces.md)
