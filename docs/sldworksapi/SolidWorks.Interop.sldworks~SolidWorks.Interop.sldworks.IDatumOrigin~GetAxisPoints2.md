# GetAxisPoints2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~GetAxisPoints2`

Gets the points that define the geometry of this datum origin.
Gets the points that define the geometry of this datum origin.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAxisPoints2() As System.Object
```

```

Dim instance As IDatumOrigin
Dim value As System.Object
 
value = instance.GetAxisPoints2()
```

```

System.object GetAxisPoints2()
```

```

System.Object^ GetAxisPoints2(); 
```

#### Return Value

Array of 8 doubles (see **Remarks**)

Remarks

The array of 8 doubles is 4 (X,Y) coordinates in drawing space:

- The first coordinate (array items 0 and 1) is the start of the X leader portion of the symbol.
- The second coordinate (array items 2 and 3) is the tip of the arrowhead on the X leader portion of the symbol.
- The third coordinate (array items 4 and 5) is the start of the Y leader portion of the symbol.
- The fourth coordinate (array items 6 and 7) is the tip of the arrowhead on the Y leader portion of the symbol.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDatumOrigin Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin.md)  
[IDatumOrigin Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin_members.md)  
[IDatumOrigin::IGetAxisPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~IGetAxisPoints2.md)  
[IDatumOrigin::SetAxisPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~SetAxisPoints.md)  
[IDatumOrigin::ISetAxisPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~ISetAxisPoints.md)
