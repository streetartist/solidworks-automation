# CreateSketchBelt Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSketchBelt`

Creates a sketch belt feature.
Creates a sketch belt feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateSketchBelt( _
   ByVal Length As System.Double, _
   ByVal Thickness As System.Double, _
   ByVal Engage As System.Integer, _
   ByVal PulleyCount As System.Integer, _
   ByVal Side1 As System.Integer, _
   ByVal Side2 As System.Integer, _
   ByVal Side3 As System.Integer, _
   ByVal Side4 As System.Integer, _
   ByVal Side5 As System.Integer, _
   ByVal Side6 As System.Integer, _
   ByVal Side7 As System.Integer, _
   ByVal Side8 As System.Integer, _
   ByVal Side9 As System.Integer, _
   ByVal Side10 As System.Integer, _
   ByVal Side11 As System.Integer, _
   ByVal Side12 As System.Integer _
) As System.Boolean
```

```

Dim instance As ISketchManager
Dim Length As System.Double
Dim Thickness As System.Double
Dim Engage As System.Integer
Dim PulleyCount As System.Integer
Dim Side1 As System.Integer
Dim Side2 As System.Integer
Dim Side3 As System.Integer
Dim Side4 As System.Integer
Dim Side5 As System.Integer
Dim Side6 As System.Integer
Dim Side7 As System.Integer
Dim Side8 As System.Integer
Dim Side9 As System.Integer
Dim Side10 As System.Integer
Dim Side11 As System.Integer
Dim Side12 As System.Integer
Dim value As System.Boolean
 
value = instance.CreateSketchBelt(Length, Thickness, Engage, PulleyCount, Side1, Side2, Side3, Side4, Side5, Side6, Side7, Side8, Side9, Side10, Side11, Side12)
```

```

System.bool CreateSketchBelt( 
   System.double Length,
   System.double Thickness,
   System.int Engage,
   System.int PulleyCount,
   System.int Side1,
   System.int Side2,
   System.int Side3,
   System.int Side4,
   System.int Side5,
   System.int Side6,
   System.int Side7,
   System.int Side8,
   System.int Side9,
   System.int Side10,
   System.int Side11,
   System.int Side12
)
```

```

System.bool CreateSketchBelt( 
   System.double Length,
   System.double Thickness,
   System.int Engage,
   System.int PulleyCount,
   System.int Side1,
   System.int Side2,
   System.int Side3,
   System.int Side4,
   System.int Side5,
   System.int Side6,
   System.int Side7,
   System.int Side8,
   System.int Side9,
   System.int Side10,
   System.int Side11,
   System.int Side12
) 
```

#### Parameters

*Length*
:   Length of the belt

*Thickness*
:   Thickness of the belt

*Engage*
:   1 to engage the belt, 0 to not

*PulleyCount*
:   Number of pulley components

*Side1*
:   Place the belt for the corresponding pulley component :

    - 0 = inside
    - 1 = outside

*Side2*
:   Place the belt for the corresponding pulley component:

    - 0 = inside
    - 1 = outside

*Side3*
:   Place the belt for the corresponding pulley component:

    - 0 = inside
    - 1 = outside

*Side4*
:   Place the belt for the corresponding pulley component:

    - 0 = inside
    - 1 = outside

*Side5*
:   Place the belt for the corresponding pulley component:

    - 0 = inside
    - 1 = outside

*Side6*
:   Place the belt for the corresponding pulley component:

    - 0 = inside
    - 1 = outside

*Side7*
:   Place the belt for the corresponding pulley component:

    - 0 = inside
    - 1 = outside

*Side8*
:   Place the belt for the corresponding pulley component:

    - 0 = inside
    - 1 = outside

*Side9*
:   Place the belt for the corresponding pulley component:

    - 0 = inside
    - 1 = outside

*Side10*
:   Place the belt for the corresponding pulley component:

    - 0 = inside
    - 1 = outside

*Side11*
:   Place the belt for the corresponding pulley component:

    - 0 = inside
    - 1 = outside

*Side12*
:   Place the belt for the corresponding pulley component:

    - 0 = inside
    - 1 = outside

#### Return Value

True the belt is created, false if not

Remarks

The order of the sides corresponds to the order of the pulleys in the selection list. For example Side1 indicates on which side of the first pulley component in the selection list you want the belt placed.  If only four pulley components exist in the sketch, then Side5 - Side12 are ignored. This method limits you to 12 pulleys.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)
