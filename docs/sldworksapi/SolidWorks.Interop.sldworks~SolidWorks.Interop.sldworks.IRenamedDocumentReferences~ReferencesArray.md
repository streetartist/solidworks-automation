# ReferencesArray Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~ReferencesArray`

Gets the pathnames of the documents with references to this renamed document.
Gets the pathnames of the documents with references to this renamed document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ReferencesArray() As System.Object
```

```

Dim instance As IRenamedDocumentReferences
Dim value As System.Object
 
value = instance.ReferencesArray()
```

```

System.object ReferencesArray()
```

```

System.Object^ ReferencesArray(); 
```

#### Return Value

Array of strings of the pathnames of the documents with references to this renamed document

Remarks

This method is only available if [IRenamedDocumentReferences::UpdateWhereUsedReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~UpdateWhereUsedReferences.md) is true.

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
[IRenamedDocumentReferences::RemoveReference Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~RemoveReference.md)
