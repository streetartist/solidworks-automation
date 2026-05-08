# UpdateStandardViews Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateStandardViews`

Changes the specified standard view to the current model view.
Changes the specified standard view to the current model view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function UpdateStandardViews( _
   ByVal ViewName As System.String, _
   ByVal ViewId As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim ViewName As System.String
Dim ViewId As System.Integer
Dim value As System.Boolean
 
value = instance.UpdateStandardViews(ViewName, ViewId)
```

```

System.bool UpdateStandardViews( 
   System.string ViewName,
   System.int ViewId
)
```

```

System.bool UpdateStandardViews( 
   System.String^ ViewName,
   System.int ViewId
) 
```

#### Parameters

*ViewName*
:   Name of the standard model view to change; empty string to use ViewId (**see Remarks**)

*ViewId*
:   View ID as defined in [swStandardViews\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swStandardViews_e.html); -1 to use ViewName (**see Remarks**)

#### Return Value

True if the standard model view update is successful, false if not

Remarks

This method works with parts and assemblies only.

If you set both ViewName and ViewId, then ViewId takes precedence if the two arguments do not resolve to the same standard model view.

This method does not support the following standard model views:

- [swStandardViews\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swStandardViews_e.html).swDimetricView
- swStandardViews\_e.swIsometricView
- swStandardViews\_e.swTrimetricView

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::ResetStandardViews Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ResetStandardViews.md)  
[IModelDoc2::ShowNamedView2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowNamedView2.md)
