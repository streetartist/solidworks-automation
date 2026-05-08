# IGetStandardViewRotation Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetStandardViewRotation`

Gets the specified view orientation matrix with respect to the Front view.
Gets the specified view orientation matrix with respect to the Front view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetStandardViewRotation( _
   ByVal ViewId As System.Integer _
) As System.Double
```

```

Dim instance As IModelDoc2
Dim ViewId As System.Integer
Dim value As System.Double
 
value = instance.IGetStandardViewRotation(ViewId)
```

```

System.double IGetStandardViewRotation( 
   System.int ViewId
)
```

```

System.double IGetStandardViewRotation( 
   System.int ViewId
) 
```

#### Parameters

*ViewId*
:   View ID that you want to evaluate as defined in [swStandardViews\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swStandardViews_e.html)

#### Return Value

Array describing the view rotation with respect to the Front view; this is an array of 9 doubles

Remarks

The end-user may have redefined the Front view to be something other than the X-Y plane.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::GetStandardViewRotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetStandardViewRotation.md)  
[IModelDocExtension::GetNamedViewRotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetNamedViewRotation.md)  
[IModelDocExtension::IGetNamedViewRotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetNamedViewRotation.md)
