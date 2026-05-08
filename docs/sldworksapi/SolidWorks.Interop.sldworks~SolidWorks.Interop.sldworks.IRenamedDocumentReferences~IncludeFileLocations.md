# IncludeFileLocations Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~IncludeFileLocations`

Gets or sets whether to search the folders listed under Referenced Documents in Tools &gt; Options &gt; System Options &gt; File Locations.
Gets or sets whether to search the folders listed under **Referenced Documents** in **Tools > Options > System Options > File Locations**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IncludeFileLocations As System.Boolean
```

```

Dim instance As IRenamedDocumentReferences
Dim value As System.Boolean
 
instance.IncludeFileLocations = value
 
value = instance.IncludeFileLocations
```

```

System.bool IncludeFileLocations {get; set;}
```

```

property System.bool IncludeFileLocations {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to search the folders listed under **Referenced Documents** in **Tools > Options > System Options > File Locations**, false to not

Remarks

This property is only available if [IRenamedDocumentReferences::UpdateWhereUsedReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~UpdateWhereUsedReferences.md) is true.

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
[IRenamedDocumentReferences::AddSearchFolder Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~AddSearchFolder.md)  
[IRenamedDocumentReferences::RemoveSearchFolder Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~RemoveSearchFolder.md)  
[IRenamedDocumentReferences::GetSearchPath Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~GetSearchPath.md)
