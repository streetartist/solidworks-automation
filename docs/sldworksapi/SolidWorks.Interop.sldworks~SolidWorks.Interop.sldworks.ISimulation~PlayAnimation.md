# PlayAnimation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation~PlayAnimation`

Obsolete. Not superseded.
Obsolete. Not superseded.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function PlayAnimation() As Animation
```

```

Dim instance As ISimulation
Dim value As Animation
 
value = instance.PlayAnimation()
```

```

Animation PlayAnimation()
```

```

Animation^ PlayAnimation(); 
```

#### Return Value

[Animation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnimation.md)

Remarks

If an animation is playing when this method is used, then this method returns the [IAnimation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnimation.md) object for that animation. To check to see if an animation is currently playing, use [ISimulation::IsAnimationPlaying](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation~IsAnimationPlaying.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation.md)  
[ISimulation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation_members.md)
