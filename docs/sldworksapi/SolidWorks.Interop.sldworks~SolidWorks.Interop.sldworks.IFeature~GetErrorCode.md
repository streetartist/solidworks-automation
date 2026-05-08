# GetErrorCode Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetErrorCode`

Obsolete. Superseded by IFeature::GetErrorCode2.
Obsolete. Superseded by [IFeature::GetErrorCode2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetErrorCode2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetErrorCode() As System.Integer
```

```

Dim instance As IFeature
Dim value As System.Integer
 
value = instance.GetErrorCode()
```

```

System.int GetErrorCode()
```

```

System.int GetErrorCode(); 
```

#### Return Value

Feature error code as defined in [swFeatureError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureError_e.html)

Remarks

This method returns many of the errors indicated by the "What's Wrong" icon seen with an invalid feature in the FeatureManager design tree.

During feature creation, you can prevent the error dialog from appearing by using  
[IModelDoc2::ShowFeatureErrorDialog](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowFeatureErrorDialog.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)
