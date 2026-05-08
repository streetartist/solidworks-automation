# ICreateSurfaceFeatureFromBodyCount2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateSurfaceFeatureFromBodyCount2`

Gets the number of surface features to create from the body.
Gets the number of surface features to create from the body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateSurfaceFeatureFromBodyCount2( _
   ByVal Body As Body2, _
   ByVal Options As System.Integer _
) As System.Integer
```

```

Dim instance As IPartDoc
Dim Body As Body2
Dim Options As System.Integer
Dim value As System.Integer
 
value = instance.ICreateSurfaceFeatureFromBodyCount2(Body, Options)
```

```

System.int ICreateSurfaceFeatureFromBodyCount2( 
   Body2 Body,
   System.int Options
)
```

```

System.int ICreateSurfaceFeatureFromBodyCount2( 
   Body2^ Body,
   System.int Options
) 
```

#### Parameters

*Body*
:   Body from which to create surface features

*Options*
:   Options as defined in [swCreateFeatureBodyOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCreateFeatureBodyOpts_e.html)

#### Return Value

Number of surface features to create from the body

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::ICreateSurfaceFeatureFromBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateSurfaceFeatureFromBody.md)  
[IPartDoc::ICreateFeatureFromBody4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateFeatureFromBody4.md)  
[IPartDoc::CreateFeatureFromBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~CreateFeatureFromBody3.md)  
[IPartDoc::CreateSurfaceFeatureFromBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~CreateSurfaceFeatureFromBody.md)
