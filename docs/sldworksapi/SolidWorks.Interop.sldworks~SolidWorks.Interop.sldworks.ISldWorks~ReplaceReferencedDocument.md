# ReplaceReferencedDocument Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ReplaceReferencedDocument`

Replaces a referenced document.
Replaces a referenced document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ReplaceReferencedDocument( _
   ByVal ReferencingDocument As System.String, _
   ByVal ReferencedDocument As System.String, _
   ByVal NewReference As System.String _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim ReferencingDocument As System.String
Dim ReferencedDocument As System.String
Dim NewReference As System.String
Dim value As System.Boolean
 
value = instance.ReplaceReferencedDocument(ReferencingDocument, ReferencedDocument, NewReference)
```

```

System.bool ReplaceReferencedDocument( 
   System.string ReferencingDocument,
   System.string ReferencedDocument,
   System.string NewReference
)
```

```

System.bool ReplaceReferencedDocument( 
   System.String^ ReferencingDocument,
   System.String^ ReferencedDocument,
   System.String^ NewReference
) 
```

#### Parameters

*ReferencingDocument*
:   Document whose references to modify; the document cannot be open

*ReferencedDocument*
:   Document is referenced by ReferencingDocument; all of its references within ReferencingDocument are replaced by NewReference

*NewReference*
:   New document used by ReferencingDocument

#### Return Value

True if the the referenced document is replaced, false if not

Remarks

Mates, dimensions, and other references might fail when the referencingDocument is opened.

If the internal ID of the ReferencedDocument does not match the internal ID of the NewReference document, then an error message is displayed when the ReferencingDocument is opened. The internal ID is a time stamp that was generated when the file was created. Unless the NewReference is actually a renamed copy of the ReferencedDocument document, then it is unlikely that the internal IDs will match.

This method does not check for the existence of the NewReference document. If the document does not exist when the ReferencingDocument is opened, then the user is warned and prompted to browse for a replacement.

The ReferencedDocument and NewReference file types must match. For example, if ReferencingDocument is an assembly with four subassemblies, you cannot replace any of the subassembly references with a part document. If you were to replace any of the subassembly references, they would need to be replaced by another SOLIDWORKS assembly document.

You might also notice that the component name, which is visible in the FeatureManager design tree, will not change to the name of the NewReference unless the proper user preference is set (Tools, Options, System Options, External References, Update component names when documents are replaced).

Example

[Replace Referenced Document (VBA)](Replace_Referenced_Document_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
