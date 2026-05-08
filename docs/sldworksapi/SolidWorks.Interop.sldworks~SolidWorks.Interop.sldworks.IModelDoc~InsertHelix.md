# InsertHelix Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertHelix`

Obsolete. Superseded by IModelDoc2::InsertHelix.
Obsolete. Superseded by [IModelDoc2::InsertHelix](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertHelix.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertHelix( _
   ByVal Reversed As System.Boolean, _
   ByVal Clockwised As System.Boolean, _
   ByVal Tapered As System.Boolean, _
   ByVal Outward As System.Boolean, _
   ByVal Helixdef As System.Integer, _
   ByVal Height As System.Double, _
   ByVal Pitch As System.Double, _
   ByVal Revolution As System.Double, _
   ByVal TaperAngle As System.Double, _
   ByVal Startangle As System.Double _
) 
```

```

Dim instance As IModelDoc
Dim Reversed As System.Boolean
Dim Clockwised As System.Boolean
Dim Tapered As System.Boolean
Dim Outward As System.Boolean
Dim Helixdef As System.Integer
Dim Height As System.Double
Dim Pitch As System.Double
Dim Revolution As System.Double
Dim TaperAngle As System.Double
Dim Startangle As System.Double
 
instance.InsertHelix(Reversed, Clockwised, Tapered, Outward, Helixdef, Height, Pitch, Revolution, TaperAngle, Startangle)
```

```

void InsertHelix( 
   System.bool Reversed,
   System.bool Clockwised,
   System.bool Tapered,
   System.bool Outward,
   System.int Helixdef,
   System.double Height,
   System.double Pitch,
   System.double Revolution,
   System.double TaperAngle,
   System.double Startangle
)
```

```

void InsertHelix( 
   System.bool Reversed,
   System.bool Clockwised,
   System.bool Tapered,
   System.bool Outward,
   System.int Helixdef,
   System.double Height,
   System.double Pitch,
   System.double Revolution,
   System.double TaperAngle,
   System.double Startangle
) 
```

#### Parameters

*Reversed*

*Clockwised*

*Tapered*

*Outward*

*Helixdef*

*Height*

*Pitch*

*Revolution*

*TaperAngle*

*Startangle*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
