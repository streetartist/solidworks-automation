# RemoveReference Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~RemoveReference`

Removes the specified reference from the list of references to update.
Removes the specified reference from the [list of references](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~ReferencesArray.md) to update.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveReference( _
   ByVal Reference As System.String _
) As System.Boolean
```

```

Dim instance As IRenamedDocumentReferences
Dim Reference As System.String
Dim value As System.Boolean
 
value = instance.RemoveReference(Reference)
```

```

System.bool RemoveReference( 
   System.string Reference
)
```

```

System.bool RemoveReference( 
   System.String^ Reference
) 
```

#### Parameters

*Reference*
:   Pathname of the reference to the renamed document to remove

#### Return Value

True if the reference to the renamed document is removed, false if not

Remarks

This method is only available if [IRenamedDocumentReferences::UpdateWhereUsedReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~UpdateWhereUsedReferences.md) is true.

Removing a reference results in that reference referencing the old file name of the document and not the new name of the document.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenamedDocumentReferences Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences.md)  
[IRenamedDocumentReferences Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences_members.md)
