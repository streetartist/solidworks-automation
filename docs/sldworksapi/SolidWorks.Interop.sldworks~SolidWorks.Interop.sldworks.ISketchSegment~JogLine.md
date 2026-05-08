# JogLine Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~JogLine`

Creates rectangular jog on the specified line.
Creates rectangular jog on the specified line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub JogLine( _
   ByVal XOnLine As System.Double, _
   ByVal YOnLine As System.Double, _
   ByVal ZOnLine As System.Double, _
   ByVal XOnJog As System.Double, _
   ByVal YOnJog As System.Double, _
   ByVal ZOnJog As System.Double _
) 
```

```

Dim instance As ISketchSegment
Dim XOnLine As System.Double
Dim YOnLine As System.Double
Dim ZOnLine As System.Double
Dim XOnJog As System.Double
Dim YOnJog As System.Double
Dim ZOnJog As System.Double
 
instance.JogLine(XOnLine, YOnLine, ZOnLine, XOnJog, YOnJog, ZOnJog)
```

```

void JogLine( 
   System.double XOnLine,
   System.double YOnLine,
   System.double ZOnLine,
   System.double XOnJog,
   System.double YOnJog,
   System.double ZOnJog
)
```

```

void JogLine( 
   System.double XOnLine,
   System.double YOnLine,
   System.double ZOnLine,
   System.double XOnJog,
   System.double YOnJog,
   System.double ZOnJog
) 
```

#### Parameters

*XOnLine*
:   x coordinate where to begin the jog on the selected line

*YOnLine*
:   y coordinate where to begin the jog on the selected line

*ZOnLine*
:   z coordinate where to begin the jog on the selected line

*XOnJog*
:   x coordinate of the width and depth of the jog

*YOnJog*
:   y coordinate of the width and depth of the jog

*ZOnJog*
:   z coordinate of the width and depth of the jog

Example

[Insert Explode Line Sketch and Jog Line (VB.NET)](Insert_Explode_Line_Sketch_and_Jog_Line_Example_VBNET.htm)  
[Insert Explode Line Sketch and Jog Line (VBA)](Insert_Explode_Line_Sketch_and_Jog_Line_Example_VB.htm)  
[Insert Explode Line Sketch and Jog Line (C#)](Insert_Explode_Line_Sketch_and_Jog_Line_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)  
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.md)  
[ISketchManager::InsertExplodeLineSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertExplodeLineSketch.md)  
[ISketchManager::Insert3DSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~Insert3DSketch.md)  
[ISketch::InsertRouteLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~InsertRouteLine.md)  
[ISketchManager::CreateLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateLine.md)
