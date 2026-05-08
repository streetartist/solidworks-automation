# RevisionNumber Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RevisionNumber`

Gets the version number of this SOLIDWORKS installation.
Gets the version number of this SOLIDWORKS installation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RevisionNumber() As System.String
```

```

Dim instance As ISldWorks
Dim value As System.String
 
value = instance.RevisionNumber()
```

```

System.string RevisionNumber()
```

```

System.String^ RevisionNumber(); 
```

#### Return Value

SOLIDWORKS version number (See **Remarks**)

Remarks

This method returns a string in the form "*major*.*minor*", where *major* is an integer (e.g., 1), and *minor* is a decimal number (e.g., 0.0).

For all SOLIDWORKS executables prior to the initial public release of SOLIDWORKS 2000, this method returns 1.0.0 (major = 1, minor = 0.0).

For the initial public release of SOLIDWORKS 2000, this method returns 8.0.0 (major = 8, minor = 0.0). For SOLIDWORKS 2000 SP1, this method returns 8.1.0, and each successive service pack or service pack hot fix of SOLIDWORKS 2000 increments the minor decimal number (e.g., SP1.1 returns **8.1.1**, SP2 returns **8.2.0**, SP3 returns **8.3.0**, etc.).

For the inital public release of SOLIDWORKS 2005, this method returns 13.0.0. For SOLIDWORKS 2005 SP0.1, it returns 13.0.1. For SOLIDWORKS 2005 SP1, it returns 13.1.0.

In general, each successive major public release increments the major number by one, each service pack increments the minor decimal number by 1.0, and each service pack hot fix increments the minor decimal number by 0.1. For the initial public release, the minor decimal number is always 0.0.

Alpha, beta, and pre-release versions return negative minor decimal numbers:

- a1:    **-1.0**
- b1:    **-2.0**
- b2:   **-3.0**
- b3:    **-4.0**
- PR1:  **-5.0** (This value might be lower or higher depending on the number of beta releases.)

For SOLIDWORKS 2015 b2, this method returns **23.-3.0**.

Example

[Create Infinite Plane (VBA)](Create_Infinite_Plane_Example_VB.htm)  
[Get Material Property Names (VBA)](Get_Material_Property_Names_Example_VB.htm)  
[Get Version Number (C#)](Get_Version_Number_Example_CSharp.htm)  
[Get Version Number (VB.NET)](Get_Version_Number_Example_VBNET.htm)  
[Get Version Number (VBA)](Get_Version_Number_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::VersionHistory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~VersionHistory.md)  
[ISldWorks::IVersionHistory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IVersionHistory.md)  
[IModelDoc2::VersionHistory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~VersionHistory.md)  
[IModelDoc2::IVersionHistory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IVersionHistory.md)  
[ISldWorks::GetBuildNumbers2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetBuildNumbers2.md)  
[Accessing SOLIDWORKS Add-in Objects](sldworksapiprogguide.chm::/Overview/Accessing_Add-ins.htm)
