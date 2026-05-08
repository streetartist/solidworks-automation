# UpdateWhereUsedReferences Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~UpdateWhereUsedReferences`

Gets or sets whether to update the references to the new file name.
Gets or sets whether to update the references to the new file name.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UpdateWhereUsedReferences As System.Boolean
```

```

Dim instance As IRenamedDocumentReferences
Dim value As System.Boolean
 
instance.UpdateWhereUsedReferences = value
 
value = instance.UpdateWhereUsedReferences
```

```

System.bool UpdateWhereUsedReferences {get; set;}
```

```

property System.bool UpdateWhereUsedReferences {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to update the references to the new file name, false to continue to reference the old file name

Example

[Rename Component and Update References (C#)](Rename_Component_and_Update_References_Example_CSharp.htm)  
[Rename Component and Update References (VB.NET)](Rename_Component_and_Update_References_Example_VBNET.htm)  
[Rename Component and Update References (VBA)](Rename_Component_and_Update_References_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenamedDocumentReferences Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences.md)  
[IRenamedDocumentReferences Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences_members.md)
