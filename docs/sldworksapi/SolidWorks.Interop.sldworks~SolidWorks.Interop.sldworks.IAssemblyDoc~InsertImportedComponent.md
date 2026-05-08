# InsertImportedComponent Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertImportedComponent`

Inserts a third-party native CAD part or assembly into the current configuration of this assembly.
Inserts a third-party native CAD part or assembly into the current configuration of this assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertImportedComponent( _
   ByVal FileName As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByRef CompInserted As System.Object _
) As System.Integer
```

```

Dim instance As IAssemblyDoc
Dim FileName As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim CompInserted As System.Object
Dim value As System.Integer
 
value = instance.InsertImportedComponent(FileName, X, Y, Z, CompInserted)
```

```

System.int InsertImportedComponent( 
   System.string FileName,
   System.double X,
   System.double Y,
   System.double Z,
   out System.object CompInserted
)
```

```

System.int InsertImportedComponent( 
   System.String^ FileName,
   System.double X,
   System.double Y,
   System.double Z,
   [Out] System.Object^ CompInserted
) 
```

#### Parameters

*FileName*
:   Full path name of the third-party native CAD file to insert

*X*
:   X-coordinate of the component center

*Y*
:   Y-coordinate of the component center

*Z*
:   Z-coordinate of the component center

*CompInserted*
:   [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md); null or Nothing if unsuccessful

#### Return Value

Error code as defined in [sw3DInterconnectImportErrors\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.sw3DInterconnectImportErrors_e.html)

Remarks

To successfully use this method, you must first turn on 3D Interconnect by either:

- Setting **Tools > Options > System Options > Import > Enable 3D Interconnect**

    - or -

- Calling [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.md)([swUserPreferenceToggle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceToggle_e.html).swMultiCAD\_Enable3DInterconnect, True)

To edit the imported assembly, save the SOLIDWORKS assembly and then use [IFeature::GetImportedFeatureParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetImportedFeatureParameters.md) and [IFeature::SetImportedFeatureParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetImportedFeatureParameters.md).

See the [IImport3DInterconnectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.md) Remarks.

If 3D Interconnect is turned off, use [IAssemblyDoc::AddComponent5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponent5.md) instead of this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[ISldWorks::LoadFile4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile4.md)  
[IPartDoc::InsertImportedFeature Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertImportedFeature.md)
