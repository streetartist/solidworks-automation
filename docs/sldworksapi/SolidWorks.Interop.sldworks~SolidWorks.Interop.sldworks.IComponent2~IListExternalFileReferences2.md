# IListExternalFileReferences2 Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IListExternalFileReferences2`

Gets the names and statuses of the external references on the component.
Gets the names and statuses of the external references on the component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IListExternalFileReferences2( _
   ByVal NumRefs As System.Integer, _
   ByRef ModelPathName As System.String, _
   ByRef CompPathName As System.String, _
   ByRef Feature As System.String, _
   ByRef DataType As System.String, _
   ByRef Status As System.Integer, _
   ByRef RefEntity As System.String, _
   ByRef FeatComp As System.String, _
   ByRef ConfigOption As System.Integer, _
   ByRef ConfigName As System.String _
) 
```

```

Dim instance As IComponent2
Dim NumRefs As System.Integer
Dim ModelPathName As System.String
Dim CompPathName As System.String
Dim Feature As System.String
Dim DataType As System.String
Dim Status As System.Integer
Dim RefEntity As System.String
Dim FeatComp As System.String
Dim ConfigOption As System.Integer
Dim ConfigName As System.String
 
instance.IListExternalFileReferences2(NumRefs, ModelPathName, CompPathName, Feature, DataType, Status, RefEntity, FeatComp, ConfigOption, ConfigName)
```

```

void IListExternalFileReferences2( 
   System.int NumRefs,
   out System.string ModelPathName,
   out System.string CompPathName,
   out System.string Feature,
   out System.string DataType,
   out System.int Status,
   out System.string RefEntity,
   out System.string FeatComp,
   out System.int ConfigOption,
   out System.string ConfigName
)
```

```

void IListExternalFileReferences2( 
   System.int NumRefs,
   [Out] System.String^ ModelPathName,
   [Out] System.String^ CompPathName,
   [Out] System.String^ Feature,
   [Out] System.String^ DataType,
   [Out] System.int Status,
   [Out] System.String^ RefEntity,
   [Out] System.String^ FeatComp,
   [Out] System.int ConfigOption,
   [Out] System.String^ ConfigName
) 
```

#### Parameters

*NumRefs*
:   Number of external references

*ModelPathName*
:   - in-process, unmanaged C++: Pointer to an array of path names of documents of size NumRefs

    - VBA, VB.NET, C#, and C++/CLI: Not supported

*CompPathName*
:   - in-process, unmanaged C++: Pointer to an array of path names of referenced components of size NumRefs

    - VBA, VB.NET, C#, and C++/CLI: Not supported

*Feature*
:   - in-process, unmanaged C++: Pointer to an array of in-context items (sketches, features, and so on) of size NumRefs
    - VBA, VB.NET, C#, and C++/CLI: Not supported

*DataType*
:   - in-process, unmanaged C+: Pointer to an array of data used to create the items (converted edge or face, converted or offset sketch entity, body, and so on) of size NumRefs
    - VBA, VB.NET, C#, and C++/CLI: Not supported

*Status*
:   - in-process, unmanaged C++: Pointer of an array of the statuses of the external references as defined in [swExternalReferenceStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swExternalReferenceStatus_e.html)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

*RefEntity*
:   - in-process, unmanaged C++: Pointer to an array of actual items being used and the names of the documents that contain the items of size NumRefs
    - VBA, VB.NET, C#, and C++/CLI: Not supported

*FeatComp*
:   - in-process, unmanaged C++: Pointer to an array of the names of the components in which the affected features exist of size NumRefs; this information is only displayed when one or more RefEntity is in a different component in an assembly and does not apply to derived parts
    - VBA, VB.NET, C#, and C++/CLI: Not supported

*ConfigOption*
:   Configuration options as defined by [swExternalFileReferencesConfig\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swExternalFileReferencesConfig_e.html)

*ConfigName*
:   Name of the configuration when configOption is swExternalFileReferencesNamedConfig

Remarks

Before calling this method, call [IComponent2::ListExternalFileReferencesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ListExternalFileReferencesCount.md) to specify NumRefs.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::ListExternalFileReferences2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ListExternalFileReferences2.md)  
[IComponent2::UpdateExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~UpdateExternalFileReferences.md)  
[IFeature::IListExternalFileReferences2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IListExternalFileReferences2.md)  
[IFeature::ListExternalFileReferences2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ListExternalFileReferences2.md)  
[IFeature::ListExternalFileReferencesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ListExternalFileReferencesCount.md)  
[IFeature::UpdateExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~UpdateExternalFileReferences.md)  
[IModelDocExtension::ListExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ListExternalFileReferences.md)  
[IModelDocExtension::ListExternalFileReferencesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ListExternalFileReferencesCount.md)  
[IModelDocExtension::UpdateExternalFileReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateExternalFileReferences.md)
