# InsertImportedFeature Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertImportedFeature`

Inserts a third-party native CAD file into this part.
Inserts a third-party native CAD file into this part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertImportedFeature( _
   ByVal FileName As System.String, _
   ByRef Errors As System.Integer _
) As System.Object
```

```

Dim instance As IPartDoc
Dim FileName As System.String
Dim Errors As System.Integer
Dim value As System.Object
 
value = instance.InsertImportedFeature(FileName, Errors)
```

```

System.object InsertImportedFeature( 
   System.string FileName,
   out System.int Errors
)
```

```

System.Object^ InsertImportedFeature( 
   System.String^ FileName,
   [Out] System.int Errors
) 
```

#### Parameters

*FileName*
:   Full path name of the third-party native CAD file to insert

*Errors*
:   Error code as defined in [swFileLoadError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFileLoadError_e.html)

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) if successful; null or Nothing otherwise

Remarks

To successfully use this method, you must first turn on 3D Interconnect by either:

- Setting **Tools > Options > System Options > Import > Enable 3D Interconnect**

    - or -

- Calling [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.md)([swUserPreferenceToggle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceToggle_e.html).swMultiCAD\_Enable3DInterconnect, True)

The feature is imported and positioned relative to the origin using coordinates of the imported file. To edit the feature, use [IFeature::GetImportedFeatureParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetImportedFeatureParameters.md) and [IFeature::SetImportedFeatureParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetImportedFeatureParameters.md).

See the [IImport3DInterconnectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.md) Remarks.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[ISldWorks::LoadFile4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile4.md)  
[IAssemblyDoc::InsertImportedComponent Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertImportedComponent.md)
