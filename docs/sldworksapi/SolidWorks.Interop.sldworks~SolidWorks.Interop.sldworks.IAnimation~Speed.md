# Speed Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnimation~Speed`

Obsolete. Not superseded.
Obsolete. Not superseded.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Speed As System.Integer
```

```

Dim instance As IAnimation
Dim value As System.Integer
 
instance.Speed = value
 
value = instance.Speed
```

```

System.int Speed {get; set;}
```

```

property System.int Speed {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Speed at which the animation plays as defined by [swAnimationPlaySpeed\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAnimationPlaySpeed_e.html)

Remarks

This property affects the duration of the animation. It allows you to specify whether  
or not to play the animation at half speed or double speed, which halves or doubles  
the animation duration.

If you use [IAnimation::Duration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnimation~Speed.md) while an animation is playing, then you might not get  
the same result as when the animation is not running.

|  |  |  |
| --- | --- | --- |
| **If you get the Animation object using...** | **And then use...** | **Then the duration...** |
| [ISimulation::Animation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation~Animation.md) | Animation::Duration | Is at the normal playing speed |
| [ISimulation::PlayAnimation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation~PlayAnimation.md) | Animation::Duration | Might be a different value because the animation is playing and the **Animation  Controller** speed may be set to **Normal**, **Slow Play**, or **Fast Play** |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnimation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnimation.md)  
[IAnimation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnimation_members.md)
