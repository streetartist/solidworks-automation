# GetFeatures Method (IFeatureFolder)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder~GetFeatures`

Gets the features in this feature folder.
Gets the features in this feature folder.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFeatures() As System.Object
```

```

Dim instance As IFeatureFolder
Dim value As System.Object
 
value = instance.GetFeatures()
```

```

System.object GetFeatures()
```

```

System.Object^ GetFeatures(); 
```

#### Return Value

Array of [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) objects

Remarks

Before calling this method, call [IFeatureFolder::GetFeatureCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder~GetFeatureCount.md) to get the size of the array returned by this method.

Example

[Get Contents of FeatureFolder (C#)](Get_Contents_of_FeatureFolder_Example_CSharp.htm)  
[Get Contents of FeatureFolder (VB.NET)](Get_Contents_of_FeatureFolder_Example_VBNET.htm)  
[Get Contents of FeatureFolder (VBA)](Get_Contents_of_FeatureFolder_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder.md)  
[IFeatureFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder_members.md)  
[IFeatureFolder::IGetFeatures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder~IGetFeatures.md)
