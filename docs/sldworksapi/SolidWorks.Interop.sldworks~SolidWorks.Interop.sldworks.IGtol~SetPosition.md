# SetPosition Method (IGtol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetPosition`

Sets the position of this GTol.
Sets the position of this GTol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetPosition( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) 
```

```

Dim instance As IGtol
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
 
instance.SetPosition(X, Y, Z)
```

```

void SetPosition( 
   System.double X,
   System.double Y,
   System.double Z
)
```

```

void SetPosition( 
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*X*
:   X location for the GTol

*Y*
:   Y location of the GTol

*Z*
:   Z location of the GTol

Example

The position is the upper-left corner of the GTol.

Example

[Get Gtol Witness Line (VBA)](Get_GTol_Witness_Line_Example_VB.htm)  
[Get Gtol Witness Line (VB.NET)](Get_GTol_Witness_Line_Example_VBNET.htm)  
[Get Gtol Witness Line (C#)](Get_GTol_Witness_Line_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)
