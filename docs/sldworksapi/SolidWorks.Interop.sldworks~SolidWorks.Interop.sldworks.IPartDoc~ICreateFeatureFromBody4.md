# ICreateFeatureFromBody4 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateFeatureFromBody4`

Creates a new imported feature from the specified temporary body.
Creates a new imported feature from the specified temporary body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateFeatureFromBody4( _
   ByVal Body As Body2, _
   ByVal MakeRefSurface As System.Boolean, _
   ByVal Options As System.Integer _
) As Feature
```

```

Dim instance As IPartDoc
Dim Body As Body2
Dim MakeRefSurface As System.Boolean
Dim Options As System.Integer
Dim value As Feature
 
value = instance.ICreateFeatureFromBody4(Body, MakeRefSurface, Options)
```

```

Feature ICreateFeatureFromBody4( 
   Body2 Body,
   System.bool MakeRefSurface,
   System.int Options
)
```

```

Feature^ ICreateFeatureFromBody4( 
   Body2^ Body,
   System.bool MakeRefSurface,
   System.int Options
) 
```

#### Parameters

*Body*
:   Temporary [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

*MakeRefSurface*
:   If the body cannot be knit to a solid or if a solid body already exists in this model, then True creates of a reference surface feature

*Options*
:   Option as defined by [swCreateFeatureBodyOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCreateFeatureBodyOpts_e.html)

#### Return Value

Newly created imported [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) or NULL if the operation fails

Remarks

This method:

- Is intended as the final call in a knitting operation. The body that results from your knitting efforts can be converted into an imported body feature in the SOLIDWORKS model.
- Is not limited to [IBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) objects obtained from knitting operations.
- Allows the application to decide how much additional work must be done to the model before creating the feature. The options listed in the swCreateFeatureBodyOpts\_e enumeration can be OR'd together to provide additional checking or simplification of the model. If you specify swCreateFeatureBodySimplify for Options, then swCreateFeatureBodyCheck is implied.

If the application passes 0 for the options argument, then the options are disabled and the model is passed without any checking. It is up to the application to ensure that the model is a valid model.

If this method fails, the error might be caused by creating a sheet (surface) body from a multiple shells body. If so, replace this method with [IPartDoc::CreateSurfaceFeatureFromBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~CreateSurfaceFeatureFromBody.md) and [IPartDoc::ICreateSurfaceFeatureFromBodyCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateSurfaceFeatureFromBodyCount2.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::CreateFeatureFromBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~CreateFeatureFromBody3.md)
