# InsertScale Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertScale`

Obsolete. Superseded by IModelDoc2::InsertScale.
Obsolete. Superseded by [IModelDoc2::InsertScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertScale.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertScale( _
   ByVal ScaleFactor_x As System.Double, _
   ByVal ScaleFactor_y As System.Double, _
   ByVal ScaleFactor_z As System.Double, _
   ByVal IsUniform As System.Boolean, _
   ByVal ScaleType As System.Integer _
) 
```

```

Dim instance As IModelDoc
Dim ScaleFactor_x As System.Double
Dim ScaleFactor_y As System.Double
Dim ScaleFactor_z As System.Double
Dim IsUniform As System.Boolean
Dim ScaleType As System.Integer
 
instance.InsertScale(ScaleFactor_x, ScaleFactor_y, ScaleFactor_z, IsUniform, ScaleType)
```

```

void InsertScale( 
   System.double ScaleFactor_x,
   System.double ScaleFactor_y,
   System.double ScaleFactor_z,
   System.bool IsUniform,
   System.int ScaleType
)
```

```

void InsertScale( 
   System.double ScaleFactor_x,
   System.double ScaleFactor_y,
   System.double ScaleFactor_z,
   System.bool IsUniform,
   System.int ScaleType
) 
```

#### Parameters

*ScaleFactor\_x*

*ScaleFactor\_y*

*ScaleFactor\_z*

*IsUniform*

*ScaleType*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
