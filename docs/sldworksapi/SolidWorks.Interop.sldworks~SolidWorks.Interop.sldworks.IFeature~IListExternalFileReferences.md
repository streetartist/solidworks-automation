# IListExternalFileReferences Method (IFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IListExternalFileReferences`

Obsolete. Superseded by IFeature::IListExternalFileReferences2.
Obsolete. Superseded by [IFeature::IListExternalFileReferences2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IListExternalFileReferences2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IListExternalFileReferences( _
   ByVal NumRefs As System.Integer, _
   ByRef ModelPathName As System.String, _
   ByRef CompPathName As System.String, _
   ByRef Feature As System.String, _
   ByRef DataType As System.String, _
   ByRef Status As System.Integer, _
   ByRef RefEntity As System.String, _
   ByRef FeatComp As System.String _
) 
```

```

Dim instance As IFeature
Dim NumRefs As System.Integer
Dim ModelPathName As System.String
Dim CompPathName As System.String
Dim Feature As System.String
Dim DataType As System.String
Dim Status As System.Integer
Dim RefEntity As System.String
Dim FeatComp As System.String
 
instance.IListExternalFileReferences(NumRefs, ModelPathName, CompPathName, Feature, DataType, Status, RefEntity, FeatComp)
```

```

void IListExternalFileReferences( 
   System.int NumRefs,
   out System.string ModelPathName,
   out System.string CompPathName,
   out System.string Feature,
   out System.string DataType,
   out System.int Status,
   out System.string RefEntity,
   out System.string FeatComp
)
```

```

void IListExternalFileReferences( 
   System.int NumRefs,
   [Out] System.String^ ModelPathName,
   [Out] System.String^ CompPathName,
   [Out] System.String^ Feature,
   [Out] System.String^ DataType,
   [Out] System.int Status,
   [Out] System.String^ RefEntity,
   [Out] System.String^ FeatComp
) 
```

#### Parameters

*NumRefs*

*ModelPathName*

*CompPathName*

*Feature*

*DataType*

*Status*

*RefEntity*

*FeatComp*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)
