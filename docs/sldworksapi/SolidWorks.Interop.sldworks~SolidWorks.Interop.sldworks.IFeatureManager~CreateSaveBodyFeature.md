# CreateSaveBodyFeature Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateSaveBodyFeature`

Creates a Save Bodies feature and creates part and assembly documents of the save bodies.
Creates a Save Bodies feature and creates part and assembly documents of the save bodies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateSaveBodyFeature( _
   ByVal Bodies As System.Object, _
   ByVal FilePaths As System.Object, _
   ByVal AssemName As System.String, _
   ByVal ConsumeBody As System.Boolean, _
   ByVal CopyCustomProperty As System.Boolean _
) As System.Object
```

```

Dim instance As IFeatureManager
Dim Bodies As System.Object
Dim FilePaths As System.Object
Dim AssemName As System.String
Dim ConsumeBody As System.Boolean
Dim CopyCustomProperty As System.Boolean
Dim value As System.Object
 
value = instance.CreateSaveBodyFeature(Bodies, FilePaths, AssemName, ConsumeBody, CopyCustomProperty)
```

```

System.object CreateSaveBodyFeature( 
   System.object Bodies,
   System.object FilePaths,
   System.string AssemName,
   System.bool ConsumeBody,
   System.bool CopyCustomProperty
)
```

```

System.Object^ CreateSaveBodyFeature( 
   System.Object^ Bodies,
   System.Object^ FilePaths,
   System.String^ AssemName,
   System.bool ConsumeBody,
   System.bool CopyCustomProperty
) 
```

#### Parameters

*Bodies*
:   :   Array of [solid bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) to save as parts (See **Remarks)**

*FilePaths*
:   :   Array of paths and filenames of the part documents to which to save Bodies

*AssemName*
:   Path and filename of the assembly document to which to save Bodies

*ConsumeBody*
:   See **Remarks**

*CopyCustomProperty*
:   See **Remarks**

#### Return Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

If any solid bodies in Bodies are invalid, they are skipped/ignored.

| For parameter... | Specify... |
| --- | --- |
| ConsumeBody | VARIANT\_TRUE (-1) to consume all bodies in the original part, VARIANT\_FALSE (0) to not |
| CopyCustomProperty | VARIANT\_TRUE (-1) to copy custom properties to the new parts, VARIANT\_FALSE (0) to not |

Example

[Create Save Bodies Feature and Create an Assembly (VBA)](Create_Save_Bodies_Feature_and_Create_Assembly_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ISaveBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData.md)
