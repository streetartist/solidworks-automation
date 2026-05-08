# EditDelete Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditDelete`

Deletes the selected items.
Deletes the selected items.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub EditDelete() 
```

```

Dim instance As IModelDoc2
 
instance.EditDelete()
```

```

void EditDelete()
```

```

void EditDelete(); 
```

Remarks

Use [IModelDocExtension::DeleteSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSelection2.md) to turn off prompting the user to confirm the deletion.

Example

[Undo Deleted Note and Fire Undo Post-Notify Event (VBA)](Undo_Deleted_Note_and_Fire_Undo_Post-Notify_Event_Example_VB.htm)  
[Undo Deleted Note and Fire Undo Post-Notify Event (VB.NET)](Undo_Deleted_Note_and_Fire_Undo_Post-Notify_Event_Example_VBNET.htm)  
[Undo Deleted Note and Fire Undo Post-Notify Event (C#)](Undo_Deleted_Note_and_Fire_Undo_Post-Notify_Event_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::EditCopy Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditCopy.md)  
[IModelDoc2::EditCut Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditCut.md)  
[IModelDoc2::Paste Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Paste.md)  
[IAssemblyDoc::DeleteSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~DeleteSelections.md)
