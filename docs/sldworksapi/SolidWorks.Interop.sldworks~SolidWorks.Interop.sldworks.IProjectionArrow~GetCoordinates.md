# GetCoordinates Method (IProjectionArrow)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~GetCoordinates`

Gets the location of this projection arrow's line and its label.
Gets the location of this projection arrow's line and its label.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCoordinates() As System.Object
```

```

Dim instance As IProjectionArrow
Dim value As System.Object
 
value = instance.GetCoordinates()
```

```

System.object GetCoordinates()
```

```

System.Object^ GetCoordinates(); 
```

#### Return Value

Array of 24 doubles containing starting and ending x,y,z points of the projection arrow and the x,y,z point for its label (see **Remarks**)

Remarks

The doubles at indexes 0, 1, and 2 are the starting point of the projection arrow; the doubles at indexes 3, 4, and 5 are the ending point of the projection arrow. The doubles at indexes 21, 22, and 23 are the label location. All other doubles in the array are duplicates of these values.

Example

[Get Arrow in Projected View (C#)](Get_Arrow_in_Projected_View_Example_CSharp.htm)  
[Get Arrow in Projected View (VB.NET)](Get_Arrow_in_Projected_View_Example_VBNET.htm)  
[Get Arrow in Projected View (VBA)](Get_Arrow_in_Projected_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IProjectionArrow Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow.md)  
[IProjectionArrow Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow_members.md)  
[IProjectionArrow::IGetCoordinates Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~IGetCoordinates.md)
