# GetUpdateStamp Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUpdateStamp`

Gets the current update stamp for this document.
Gets the current update stamp for this document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUpdateStamp() As System.Integer
```

```

Dim instance As IModelDoc2
Dim value As System.Integer
 
value = instance.GetUpdateStamp()
```

```

System.int GetUpdateStamp()
```

```

System.int GetUpdateStamp(); 
```

#### Return Value

Current update stamp value for this document

Remarks

The update stamp is an integer form of a time stamp. The update stamp is incremented for model state changes (i.e., suppress or unsuppress, configuration changes, feature changes, etc.) and for geometric changes (i.e., anything that requires a rebuild). This time stamp is not incremented for operations such as color changes, feature or configuration name changes, etc.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IFeature::GetUpdateStamp Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetUpdateStamp.md)
