# InsertSheetMetalJog Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSheetMetalJog`

Inserts a sheet metal jog in the current model document.
Inserts a sheet metal jog in the current model document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertSheetMetalJog( _
   ByVal Angle As System.Double, _
   ByVal Radius As System.Double, _
   ByVal OffsetDist As System.Double, _
   ByVal FlipDir As System.Boolean, _
   ByVal FixProjLen As System.Boolean, _
   ByVal DimPos As System.Short, _
   ByVal BendPos As System.Short _
) 
```

```

Dim instance As IModelDoc2
Dim Angle As System.Double
Dim Radius As System.Double
Dim OffsetDist As System.Double
Dim FlipDir As System.Boolean
Dim FixProjLen As System.Boolean
Dim DimPos As System.Short
Dim BendPos As System.Short
 
instance.InsertSheetMetalJog(Angle, Radius, OffsetDist, FlipDir, FixProjLen, DimPos, BendPos)
```

```

void InsertSheetMetalJog( 
   System.double Angle,
   System.double Radius,
   System.double OffsetDist,
   System.bool FlipDir,
   System.bool FixProjLen,
   System.short DimPos,
   System.short BendPos
)
```

```

void InsertSheetMetalJog( 
   System.double Angle,
   System.double Radius,
   System.double OffsetDist,
   System.bool FlipDir,
   System.bool FixProjLen,
   System.short DimPos,
   System.short BendPos
) 
```

#### Parameters

*Angle*
:   Jog angle

*Radius*
:   Jog radius

*OffsetDist*
:   Offset distance

*FlipDir*
:   True flips the jog direction, false does not

*FixProjLen*
:   True fixes the projected length, false does not

*DimPos*
:   Dimension position

*BendPos*
:   Bend position

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.md)
