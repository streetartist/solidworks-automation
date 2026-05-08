# AddSearchFolder Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~AddSearchFolder`

Adds the specified folder in which to search for documents whose references to update.
Adds the specified folder in which to search for documents whose references to update.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddSearchFolder( _
   ByVal Folder As System.String _
) As System.Boolean
```

```

Dim instance As IRenamedDocumentReferences
Dim Folder As System.String
Dim value As System.Boolean
 
value = instance.AddSearchFolder(Folder)
```

```

System.bool AddSearchFolder( 
   System.string Folder
)
```

```

System.bool AddSearchFolder( 
   System.String^ Folder
) 
```

#### Parameters

*Folder*
:   Folder in which to search for documents whose references to update

#### Return Value

True if the specified folder is added to the search, false if not

Remarks

This method is only available if [IRenamedDocumentReferences::UpdateWhereUsedReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~UpdateWhereUsedReferences.md) is true.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenamedDocumentReferences Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences.md)  
[IRenamedDocumentReferences Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences_members.md)  
[IRenamedDocumentReferences::RemoveSearchFolder Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~RemoveSearchFolder.md)  
[IRenamedDocumentReferences::IncludeFileLocations Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~IncludeFileLocations.md)  
[IRenamedDocumentReferences::GetSearchPath Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~GetSearchPath.md)
