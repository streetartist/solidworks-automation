# SetAutomaticCutList Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~SetAutomaticCutList`

Sets whether to automatically generate a cut list when the first weldment feature is inserted in a part.
Sets whether to automatically generate a cut list when the first weldment feature is inserted in a part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetAutomaticCutList( _
   ByVal CutList As System.Boolean _
) As System.Boolean
```

```

Dim instance As IBodyFolder
Dim CutList As System.Boolean
Dim value As System.Boolean
 
value = instance.SetAutomaticCutList(CutList)
```

```

System.bool SetAutomaticCutList( 
   System.bool CutList
)
```

```

System.bool SetAutomaticCutList( 
   System.bool CutList
) 
```

#### Parameters

*CutList*
:   True to automatically generate a cut list, false to not

#### Return Value

True if enabled, false if not (see **Remarks**)

Remarks

Use [IBodyFolder::GetAutomaticCutList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetAutomaticCutList.md) to find out if automatic generation of a cut list is enabled.

This method returns false if:

- the part does not contain a weldment feature. Use [IPartDoc::IsWeldment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IsWeldment.md) to find out  
  if the part contains this feature.
- a cut list folder already exists in the part. You must delete the cut list before  
  you can enable automatic generation.

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
