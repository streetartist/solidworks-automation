# GetExternalDocuments Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetExternalDocuments`

Gets the paths and filenames of the non-SOLIDWORKS files added to Pack And Go.
Gets the paths and filenames of the non-SOLIDWORKS files added to Pack And Go.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetExternalDocuments( _
   ByRef DocumentNames As System.Object _
) As System.Boolean
```

```

Dim instance As IPackAndGo
Dim DocumentNames As System.Object
Dim value As System.Boolean
 
value = instance.GetExternalDocuments(DocumentNames)
```

```

System.bool GetExternalDocuments( 
   out System.object DocumentNames
)
```

```

System.bool GetExternalDocuments( 
   [Out] System.Object^ DocumentNames
) 
```

#### Parameters

*DocumentNames*
:   Array of strings of the paths and filenames of the non-SOLIDWORKS files added to Pack and Go

#### Return Value

True if the paths and filenames of the non-SOLIDWORKS files are returned, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.md)  
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.md)  
[IPackAndGo::AddExternalDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~AddExternalDocuments.md)
