# InsertGlobalBoundingBox Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertGlobalBoundingBox`

Obsolete. See IFeatureManager::CreateDefinition and IBoundingBoxFeatureData.
Obsolete. See [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.md) and [IBoundingBoxFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertGlobalBoundingBox( _
   ByVal BBoxType As System.Integer, _
   ByVal IncludeHiddenBodies As System.Boolean, _
   ByVal IncludeSurfaceBodies As System.Boolean, _
   ByRef Status As System.Integer _
) As System.Object
```

```

Dim instance As IFeatureManager
Dim BBoxType As System.Integer
Dim IncludeHiddenBodies As System.Boolean
Dim IncludeSurfaceBodies As System.Boolean
Dim Status As System.Integer
Dim value As System.Object
 
value = instance.InsertGlobalBoundingBox(BBoxType, IncludeHiddenBodies, IncludeSurfaceBodies, Status)
```

```

System.object InsertGlobalBoundingBox( 
   System.int BBoxType,
   System.bool IncludeHiddenBodies,
   System.bool IncludeSurfaceBodies,
   out System.int Status
)
```

```

System.Object^ InsertGlobalBoundingBox( 
   System.int BBoxType,
   System.bool IncludeHiddenBodies,
   System.bool IncludeSurfaceBodies,
   [Out] System.int Status
) 
```

#### Parameters

*BBoxType*
:   Bounding Box fit type as defined in [swGlobalBoundingBoxFitOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGlobalBoundingBoxFitOptions_e.html) (see **Remarks**)

*IncludeHiddenBodies*
:   True to include hidden bodies, false to not

*IncludeSurfaceBodies*
:   True to include surfaces, false to not

*Status*
:   Status as defined by [swGlobalBoundingBoxResult\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGlobalBoundingBoxResult_e.html)

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

If BBoxType is set to swGlobalBoundingBoxFitOptions\_e.swBoundingBoxType\_CustomPlane, then select a face or plane using [IModelDocExtension::SelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByRay.md) with TypeWanted set to [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html).swSelFACES before calling this method.

To display or hide the Bounding Box sketch, call [IModelDoc2::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetUserPreferenceToggle.md) to set [swUserPreferenceToggle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceToggle_e.html).swViewDispGlobalBBox to true or false, respectively.

After calling this method, use [IModelDoc2::ClearSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClearSelection2.md) to clear the selection made when the Bounding Box is created.

Example

```

'VBA 
```

```

Dim swApp As SldWorks.SldWorks  
Dim Part As SldWorks.ModelDoc2  
Dim boolstatus As Boolean  
Dim longstatus As Long  
Option Explicit
```

```

Sub main()  
      
    Set swApp = Application.SldWorks  
    Set Part = swApp.ActiveDoc 
```

```

    ' Display the Bounding Box sketch  
    boolstatus = Part.SetUserPreferenceToggle)swViewDispGlobalBBox, True)  
      
    Dim BoundingBox As SldWorks.Feature  
    Set BoundingBox = Part.FeatureManager.InsertGlobalBoundingBox(swBoundingBoxType_BestFit, True, False, longstatus)
```

```

    Part.ClearSelection2 True
```

```

    ' Hide the Bounding Box sketch  
    boolstatus = Part.SetUserPreferenceToggle)swViewDispGlobalBBox, False)
```

```

End Sub
```

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
