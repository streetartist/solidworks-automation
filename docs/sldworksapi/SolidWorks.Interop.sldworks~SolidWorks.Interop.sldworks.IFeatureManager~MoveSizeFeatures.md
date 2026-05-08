# MoveSizeFeatures Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~MoveSizeFeatures`

Shows or hides the feature Instant3D.
Shows or hides the feature Instant3D.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MoveSizeFeatures As System.Boolean
```

```

Dim instance As IFeatureManager
Dim value As System.Boolean
 
instance.MoveSizeFeatures = value
 
value = instance.MoveSizeFeatures
```

```

System.bool MoveSizeFeatures {get; set;}
```

```

property System.bool MoveSizeFeatures {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to enable Instant3D, false to not

Example

Option Explicit

Dim swApp As SldWorks.SldWorks

Dim swModel As SldWorks.ModelDoc2

Dim swFeatMgr As SldWorks.FeatureManager

Sub main()

Set swApp = Application.SldWorks

Set swModel = swApp.ActiveDoc

Set swFeatMgr = swModel.FeatureManager

Debug.Print "Is Instant3D enabled? " & swFeatMgr.MoveSizeFeatures

swFeatMgr.MoveSizeFeatures = False

Debug.Print "Is Instant3D enabled? " & swFeatMgr.MoveSizeFeatures

swFeatMgr.MoveSizeFeatures = True

Debug.Print "Is Instant3D enabled? " & swFeatMgr.MoveSizeFeatures

End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
