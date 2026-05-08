# Stretch Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Stretch`

Stretch the selected entities.
Stretch the selected entities.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Stretch( _
   ByVal KeepRelations As System.Boolean, _
   ByVal BaseX As System.Double, _
   ByVal BaseY As System.Double, _
   ByVal DestX As System.Double, _
   ByVal DestY As System.Double _
) 
```

```

Dim instance As IModelDocExtension
Dim KeepRelations As System.Boolean
Dim BaseX As System.Double
Dim BaseY As System.Double
Dim DestX As System.Double
Dim DestY As System.Double
 
instance.Stretch(KeepRelations, BaseX, BaseY, DestX, DestY)
```

```

void Stretch( 
   System.bool KeepRelations,
   System.double BaseX,
   System.double BaseY,
   System.double DestX,
   System.double DestY
)
```

```

void Stretch( 
   System.bool KeepRelations,
   System.double BaseX,
   System.double BaseY,
   System.double DestX,
   System.double DestY
) 
```

#### Parameters

*KeepRelations*
:   True to keep the sketch relations intact, false to sever them

*BaseX*
:   x coordinate of the base point

*BaseY*
:   y coordinate of the base point

*DestX*
:   x coordinate of the destination stretch

*DestY*
:   y coordinate of the destination of the stretch

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
