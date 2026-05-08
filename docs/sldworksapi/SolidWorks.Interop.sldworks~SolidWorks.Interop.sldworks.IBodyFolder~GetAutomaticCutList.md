# GetAutomaticCutList Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetAutomaticCutList`

Gets whether to automatically generate a cut list when the first weldment feature is inserted in a part.
Gets whether to automatically generate a cut list when the first weldment feature is inserted in a part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAutomaticCutList() As System.Boolean
```

```

Dim instance As IBodyFolder
Dim value As System.Boolean
 
value = instance.GetAutomaticCutList()
```

```

System.bool GetAutomaticCutList()
```

```

System.bool GetAutomaticCutList(); 
```

#### Return Value

True to automatically generate a cut list, false to not

Remarks

By default, a cut list is automatically generated in new weldment parts. Use [IBodyFolder::SetAutomaticCutList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~SetAutomaticCutList.md) to change the default. Use [IPartDoc::IsWeldment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IsWeldment.md) to get whether the part contains a weldment feature.

Example

See the [IBodyFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBodyFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.md)  
[IBodyFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder_members.md)  
[IBodyFolder::UpdateCutList Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~UpdateCutList.md)  
[IBodyFolder::GetCutListType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetCutListType.md)  
[IBodyFolder::GetCutListSortOptions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetCutListSortOptions.md)
