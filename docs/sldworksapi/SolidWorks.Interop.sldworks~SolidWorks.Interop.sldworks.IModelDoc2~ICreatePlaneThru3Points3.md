# ICreatePlaneThru3Points3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneThru3Points3`

Obsolete. Superseded by IFeatureManager::InsertRefPlane.
Obsolete. Superseded by [IFeatureManager::InsertRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertRefPlane.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreatePlaneThru3Points3( _
   ByVal AutoSize As System.Boolean _
) As RefPlane
```

```

Dim instance As IModelDoc2
Dim AutoSize As System.Boolean
Dim value As RefPlane
 
value = instance.ICreatePlaneThru3Points3(AutoSize)
```

```

RefPlane ICreatePlaneThru3Points3( 
   System.bool AutoSize
)
```

```

RefPlane^ ICreatePlaneThru3Points3( 
   System.bool AutoSize
) 
```

#### Parameters

*AutoSize*
:   True to automatically size the plane, false to not

#### Return Value

Newly created [reference plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)

Remarks

This method uses the current document setting for displaying the reference plane. If display of reference planes is disabled, then you do not see the reference plane on the screen. If display of reference planes is enabled, then you see it. [IModelDocExtension::GetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceToggle.md) swDisplayPlanes and [IModelDocExtension::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceToggle.md) swDisplayPlanes get or set this display preference.

 

This method does not select the reference plane after it is created. Objects that are selected before running this method are still selected when the method completes, not the newly created reference plane.

 

This method returns an IRefPlane object. This object can then be used for subsequent operations on the reference plane feature. Having a IRefPlane object may not be useful, except that it is a feature, which is an entity, so methods available on those objects are available. For an OLE user, those functions are directly accessible; for a COM user, those functions are available via QueryInterface. For example, to select the reference plane, use [IEntity::Select4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~Select4.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::CreatePlaneAtAngle3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneAtAngle3.md)  
[IModelDoc2::CreatePlaneAtOffset3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneAtOffset3.md)  
[IModelDoc2::CreatePlaneAtSurface3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneAtSurface3.md)  
[IModelDoc2::CreatePlaneFixed2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneFixed2.md)  
[IModelDoc2::CreatePlanePerCurveAndPassPoint3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlanePerCurveAndPassPoint3.md)  
[IModelDoc2::CreatePlaneThru3Points3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneThru3Points3.md)  
[IModelDoc2::CreatePlaneThruLineAndPt Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneThruLineAndPt.md)  
[IModelDoc2::CreatePlaneThruPtParallelToPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneThruPtParallelToPlane.md)  
[IModelDoc2::GetVisibilityOfConstructPlanes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetVisibilityOfConstructPlanes.md)  
[IModelDoc2::ICreatePlaneAtAngle3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneAtAngle3.md)  
[IModelDoc2::ICreatePlaneAtOffset3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneAtOffset3.md)  
[IModelDoc2::ICreatePlaneAtSurface3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneAtSurface3.md)  
[IModelDoc2::ICreatePlaneFixed2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneFixed2.md)  
[IModelDoc2::ICreatePlanePerCurveAndPassPoint3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlanePerCurveAndPassPoint3.md)  
[IModelDoc2::ICreatePlaneThru3Points3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneThru3Points3.md)  
[IModelDoc2::ICreatePlaneThruLineAndPt Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneThruLineAndPt.md)  
[IModelDoc2::ICreatePlaneThruPtParallelToPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneThruPtParallelToPlane.md)  
[IModelDoc2::ViewDispRefplanes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewDispRefplanes.md)
