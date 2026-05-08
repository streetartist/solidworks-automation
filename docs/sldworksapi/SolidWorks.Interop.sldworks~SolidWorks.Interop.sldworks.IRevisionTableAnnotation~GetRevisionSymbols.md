# GetRevisionSymbols Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetRevisionSymbols`

Gets the revision symbols associated with the specified revision ID.
Gets the revision symbols associated with the specified revision ID.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRevisionSymbols( _
   ByVal RevisionId As System.Integer _
) As System.Object
```

```

Dim instance As IRevisionTableAnnotation
Dim RevisionId As System.Integer
Dim value As System.Object
 
value = instance.GetRevisionSymbols(RevisionId)
```

```

System.object GetRevisionSymbols( 
   System.int RevisionId
)
```

```

System.Object^ GetRevisionSymbols( 
   System.int RevisionId
) 
```

#### Parameters

*RevisionId*
:   Revision ID

#### Return Value

Array of revision symbols

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRevisionTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation.md)  
[IRevisionTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation_members.md)  
[IRevisionTableAnnotation::GetRevisionSymbolCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetRevisionSymbolCount.md)  
[IRevisionTableAnnotation::IGetRevisionSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~IGetRevisionSymbols.md)  
[IRevisionTableAnnotation::CurrentRevision Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~CurrentRevision.md)
