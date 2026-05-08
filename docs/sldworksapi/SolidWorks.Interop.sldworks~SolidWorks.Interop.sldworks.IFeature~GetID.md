# GetID Method (IFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetID`

Gets the feature ID of this feature.
Gets the feature ID of this feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetID() As System.Integer
```

```

Dim instance As IFeature
Dim value As System.Integer
 
value = instance.GetID()
```

```

System.int GetID()
```

```

System.int GetID(); 
```

#### Return Value

Feature ID of this feature

Remarks

A feature ID:

- is unique within the document.
- is persistent across SOLIDWORKS sessions and never changes, even if you [change the name of the feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Name.md).
- can be used to identify a specific feature when multiple features exist in a model.
- cannot be assigned by users.
- is not the same as a [persistent reference ID](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm). You can get a feature using its persistent reference ID, but you cannot get a feature using this method.

Example

[Get Type of Instant3D Feature (C#)](Get_Type_of_Instant3D_Feature_Example_CSharp.htm)  
[Get Type of Instant3D Feature (VB.NET)](Get_Type_of_Instant3D_Feature_Example_VBNET.htm)  
[Get Type of Instant3D Feature (VBA)](Get_Type_of_Instant3D_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)
