# CreateSurfaceFeatureFromBody Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~CreateSurfaceFeatureFromBody`

Creates a surface feature from a body.
Creates a surface feature from a body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateSurfaceFeatureFromBody( _
   ByVal Body As System.Object, _
   ByVal Options As System.Integer _
) As System.Object
```

```

Dim instance As IPartDoc
Dim Body As System.Object
Dim Options As System.Integer
Dim value As System.Object
 
value = instance.CreateSurfaceFeatureFromBody(Body, Options)
```

```

System.object CreateSurfaceFeatureFromBody( 
   System.object Body,
   System.int Options
)
```

```

System.Object^ CreateSurfaceFeatureFromBody( 
   System.Object^ Body,
   System.int Options
) 
```

#### Parameters

*Body*
:   [Body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) from which to create surface feature

*Options*
:   Surface feature options as defined in [swCreateFeatureBodyOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCreateFeatureBodyOpts_e.html)

#### Return Value

Surface [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) array

Example

[Create Loft Surface Body and Change Into Feature (VBA)](Create_Loft_Surface_Body_and_Change_Into_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::ICreateSurfaceFeatureFromBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateSurfaceFeatureFromBody.md)  
[IPartDoc::ICreateSurfaceFeatureFromBodyCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateSurfaceFeatureFromBodyCount2.md)  
[IPartDoc::ICreateFeatureFromBody4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateFeatureFromBody4.md)  
[IPartDoc::CreateFeatureFromBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~CreateFeatureFromBody3.md)
