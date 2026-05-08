# IListAuxiliaryExternalFileReferences Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IListAuxiliaryExternalFileReferences`

Gets the names of auxiliary external file references for this model.
Gets the names of auxiliary external file references for this model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IListAuxiliaryExternalFileReferences( _
   ByVal NumRefs As System.Integer, _
   ByRef Feature As System.String, _
   ByRef ExternalFileName As System.String _
) 
```

```

Dim instance As IModelDoc2
Dim NumRefs As System.Integer
Dim Feature As System.String
Dim ExternalFileName As System.String
 
instance.IListAuxiliaryExternalFileReferences(NumRefs, Feature, ExternalFileName)
```

```

void IListAuxiliaryExternalFileReferences( 
   System.int NumRefs,
   out System.string Feature,
   out System.string ExternalFileName
)
```

```

void IListAuxiliaryExternalFileReferences( 
   System.int NumRefs,
   [Out] System.String^ Feature,
   [Out] System.String^ ExternalFileName
) 
```

#### Parameters

*NumRefs*
:   Number of external references

*Feature*
:   Array of size NumRefs containing the names of features that include auxiliary external references

*ExternalFileName*
:   Array of size NumRefs containing the names of the auxiliary external files

Remarks

Call [IModelDoc2::ListAuxiliaryExtenalFileReferencesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ListAuxiliaryExternalFileReferencesCount.md) before calling of this method to determine the size of the arrays.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::ListAuxiliaryExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ListAuxiliaryExternalFileReferences.md)  
[IModelDocExtension::IListExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IListExternalFileReferences.md)  
[IModelDocExtension::ListExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ListExternalFileReferences.md)  
[IModelDoc2::ListAuxiliaryExternalFileReferencesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ListAuxiliaryExternalFileReferencesCount.md)  
[IModelDoc2::LockAllExternalReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LockAllExternalReferences.md)
