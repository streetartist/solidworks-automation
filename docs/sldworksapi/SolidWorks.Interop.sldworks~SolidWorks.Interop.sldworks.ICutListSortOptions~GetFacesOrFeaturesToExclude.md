# GetFacesOrFeaturesToExclude Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions~GetFacesOrFeaturesToExclude`

Gets the faces or features to exclude from cut list sorting.
Gets the faces or features to exclude from cut list sorting.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFacesOrFeaturesToExclude() As System.Object
```

```

Dim instance As ICutListSortOptions
Dim value As System.Object
 
value = instance.GetFacesOrFeaturesToExclude()
```

```

System.object GetFacesOrFeaturesToExclude()
```

```

System.Object^ GetFacesOrFeaturesToExclude(); 
```

#### Return Value

Array of [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) or [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) to exclude

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICutListSortOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions.md)  
[ICutListSortOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions_members.md)  
[ICutListSortOptions::SetFacesOrFeaturesToExclude Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions~SetFacesOrFeaturesToExclude.md)
