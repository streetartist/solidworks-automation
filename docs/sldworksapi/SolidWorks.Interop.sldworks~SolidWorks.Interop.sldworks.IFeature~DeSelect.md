# DeSelect Method (IFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~DeSelect`

Deselects this feature.
Deselects this feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeSelect() As System.Boolean
```

```

Dim instance As IFeature
Dim value As System.Boolean
 
value = instance.DeSelect()
```

```

System.bool DeSelect()
```

```

System.bool DeSelect(); 
```

#### Return Value

True if the feature is deselected successfully, false if not

Remarks

Use [IModelDoc2::DeSelectByID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeSelectByID.md) instead of this method. This method does not work well when a PropertyManager page is open or a command is running. IModelDoc2::DeSelectByID handles selection correctly whether or not a command is running.

Example

[Get Section Properties for Faces from Section Planes (VBA)](Get_Section_Properties_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::Select2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Select2.md)  
[IFeature::GetSpecificFeature2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.md)
