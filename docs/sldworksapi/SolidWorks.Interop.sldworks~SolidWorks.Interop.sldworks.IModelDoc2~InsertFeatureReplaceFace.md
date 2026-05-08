# InsertFeatureReplaceFace Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertFeatureReplaceFace`

Creates a Replace Face feature.
Creates a Replace Face feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertFeatureReplaceFace() 
```

```

Dim instance As IModelDoc2
 
instance.InsertFeatureReplaceFace()
```

```

void InsertFeatureReplaceFace()
```

```

void InsertFeatureReplaceFace(); 
```

#### Return Value

True if the edges match, false if not

Remarks

Before calling this method, select the faces to replace by calling [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) with Marks of 1 and select the replacement surfaces by calling IModelDocExtension::SelectByID2 with Marks of 2.

See SOLIDWORKS Help for details about the Replace Face feature.

Example

[Create Replace Face Feature (VBA)](Replace_Face_Example_VB.htm)  
[Create Replace Face Feature (VB.NET)](Replace_Face_Example_VBNET.htm)  
[Create Replace Face Feature (C#)](Replace_Face_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IReplaceFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData.md)
