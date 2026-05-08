# IsBendLineNote Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsBendLineNote`

Gets whether this note is a bendline note.
Gets whether this note is a bendline note.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property IsBendLineNote As System.Boolean
```

```

Dim instance As INote
Dim value As System.Boolean
 
value = instance.IsBendLineNote
```

```

System.bool IsBendLineNote {get;}
```

```

property System.bool IsBendLineNote {
   System.bool get();
}
```

#### Property Value

True if note is a bendline note, false if not

Example

[Merge and Unmerge Bend Tags (C#)](Merge_and_Unmerge_Bend_Tags_Example_CSharp.htm)  
[Merge and Unmerge Bend Tags (VB.NET)](Merge_and_Unmerge_Bend_Tags_Example_VBNET.htm)  
[Merge and Unmerge Bend Tags (VBA)](Merge_and_Unmerge_Bend_Tags_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)  
[INote::GetBendLineValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBendLineValues.md)  
[IView::MergeBendTags Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~MergeBendTags.md)
