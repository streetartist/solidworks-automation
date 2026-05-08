# Animation Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation~Animation`

Obsolete. Not superseded.
Obsolete. Not superseded.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Animation As Animation
```

```

Dim instance As ISimulation
Dim value As Animation
 
value = instance.Animation
```

```

Animation Animation {get;}
```

```

property Animation^ Animation {
   Animation^ get();
}
```

#### Property Value

[Animation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnimation.md)

Remarks

|  |  |
| --- | --- |
| **To...** | **Then..**. |
| Get the duration of an animation | Use [IAnimation::Duration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnimation~Duration.md) after using this property |
| Play the animation | Use [IAnimation::Play](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnimation~Play.md) after using this property |
| Display the Animation Controller pop-up toolbar | Use [ISimulation::PlayAnimation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation~PlayAnimation.md) instead of using this property |

NOTE: Use only the following IAnimation property and method with ISimulation::Animation: IAnimation::Duration and IAnimation::PlayAnimation. The other IAnimation properties and methods do nothing with an IAnimation object returned by ISimlulation::Animation because they expect an animation to be playing. Use [ISimluation::IsAnimationPlaying](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation~IsAnimationPlaying.md) to determine whether an animation is playing.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation.md)  
[ISimulation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation_members.md)
