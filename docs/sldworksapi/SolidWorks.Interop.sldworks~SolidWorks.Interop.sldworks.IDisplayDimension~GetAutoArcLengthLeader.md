# GetAutoArcLengthLeader Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetAutoArcLengthLeader`

Gets whether the leader style of this arc-length dimension is being automatically selected or selected by the user.
Gets whether the leader style of this arc-length dimension is being automatically selected or selected by the user.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAutoArcLengthLeader() As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
value = instance.GetAutoArcLengthLeader()
```

```

System.bool GetAutoArcLengthLeader()
```

```

System.bool GetAutoArcLengthLeader(); 
```

#### Return Value

True if the leader style is selected automatically , false if the leader style is selected by the user

Remarks

The leader style of an arc-length dimension is specific to each display dimension. It can be parallel (the leaders are parallel to each other) or radial (the leaders are perpendicular to the extension line and would extend through the center of the arc). SOLIDWORKS can automatically select the style, or it can be specified by the user. Use IDisplayDimension::GetAutoArcLengthLeader to determine whether the leader type is selected automatically.

This method gets the leader style stored on this display dimension. If this display dimension is set to select the leader type automatically, then this method might return a value that is different from what is displayed.

This method applies to only arc length dimensions. It returns -1 if you run it on any other types of dimensions.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::GetArcLengthLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetArcLengthLeader.md)  
[IDisplayDimension::SetArcLengthLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetArcLengthLeader.md)
