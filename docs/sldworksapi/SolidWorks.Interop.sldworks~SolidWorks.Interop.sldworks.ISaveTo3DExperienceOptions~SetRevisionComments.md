# SetRevisionComments Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveTo3DExperienceOptions~SetRevisionComments`

Sets the specified revision comments when saving a document in SOLIDWORKS Connected.
Sets the specified revision comments when saving a document in [SOLIDWORKS Connected](sldworksapiprogguide.chm::/Overview/SOLIDWORKS_Connected.htm).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetRevisionComments( _
   ByVal RevisionComments As System.String _
) As System.Boolean
```

```

Dim instance As ISaveTo3DExperienceOptions
Dim RevisionComments As System.String
Dim value As System.Boolean
 
value = instance.SetRevisionComments(RevisionComments)
```

```

System.bool SetRevisionComments( 
   System.string RevisionComments
)
```

```

System.bool SetRevisionComments( 
   System.String^ RevisionComments
) 
```

#### Parameters

*RevisionComments*
:   Save comments

#### Return Value

True if the document saved successfully, false if not

Example

See the [IPLMObjectSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPLMObjectSpecification.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISaveTo3DExperienceOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveTo3DExperienceOptions.md)  
[ISaveTo3DExperienceOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveTo3DExperienceOptions_members.md)
