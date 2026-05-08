# RunMacro2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunMacro2`

Runs a macro from a project file.
Runs a macro from a project file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RunMacro2( _
   ByVal FilePathName As System.String, _
   ByVal ModuleName As System.String, _
   ByVal ProcedureName As System.String, _
   ByVal Options As System.Integer, _
   ByRef Error As System.Integer _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim FilePathName As System.String
Dim ModuleName As System.String
Dim ProcedureName As System.String
Dim Options As System.Integer
Dim Error As System.Integer
Dim value As System.Boolean
 
value = instance.RunMacro2(FilePathName, ModuleName, ProcedureName, Options, Error)
```

```

System.bool RunMacro2( 
   System.string FilePathName,
   System.string ModuleName,
   System.string ProcedureName,
   System.int Options,
   out System.int Error
)
```

```

System.bool RunMacro2( 
   System.String^ FilePathName,
   System.String^ ModuleName,
   System.String^ ProcedureName,
   System.int Options,
   [Out] System.int Error
) 
```

#### Parameters

*FilePathName*
:   Path and filename of the project file containing the macro

*ModuleName*
:   Name of the module in the macro

*ProcedureName*
:   Name of the procedure in the module

*Options*
:   Option as defined [swRunMacroOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRunMacroOption_e.html) (supports VBA macros only)

*Error*
:   Error as defined by [swRunMacroError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRunMacroError_e.html) (supports VBA macros only)

#### Return Value

True if macro runs, false if not

Remarks

If you specify swRunMacroUnloadAfterRun for Options, then the macro is unloaded from the VBA IDE after running.

Use the path and filename of the compiled DLL for the FilePathName argument for a .NET macro. By default, the procedure is called **Main** in a C# macro. Because C# is case sensitive, you must specify **Main** for ProcedureName in this method.. See **Running a C# DLL from VBA** in the **Example** section.

Running a macro from an add-in application, standalone .exe, or VBA macro is supported. Running a .NET macro from a .NET macro is also supported, but only if both .NET macros were created using the same VSTA version.

See [SOLIDWORKS Macros](sldworksAPIProgGuide.chm::/GettingStarted/SOLIDWORKS_Macros.htm) for details.

Example

**Visual Basic for Applications (VBA)**

1. Create two VBA macros using the following code samples.
2. Store **RunMacroSub.swp** in **c:\test**.
3. Run **RunMacro.swp**.

'----------------------------  
' RunMacro.swp  
'---------------------------

Option Explicit  
Dim swApp As SldWorks.SldWorks  
Dim boolstatus As Boolean  
Sub main()  
   Set swApp = Application.SldWorks  
   Dim runMacroError As Long  
   boolstatus = swApp.**RunMacro2**("c:\test\RunMacroSub.swp", "RunMacroSub1", "main",   swRunMacroUnloadAfterRun, runMacroError)  
End Sub

'---------------------------------------  
' RunMacroSub.swp  
'---------------------------------------  
Option Explicit  
Dim swApp As SldWorks.SldWorks  
Sub alternate()  
   Set swApp = Application.SldWorks  
   swApp.SendMsgToUser "RunMacroSub1:alternate() called."  
End Sub  
Sub main()  
   Set swApp = Application.SldWorks  
   swApp.SendMsgToUser "RunMacroSub1:main() called."  
End Sub

**Running a C# DLL from VBA**

boolstatus = Me.swApp.**RunMacro2**('C:\Test\CSharpMacro\SwMacro\bin\Release\CSharpMacro.dll',

 '', 'Main',  swRunMacroOption\_e.swRunMacroDefault, runMacroError)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetCurrentMacroPathFolder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentMacroPathFolder.md)  
[ISldWorks::GetCurrentMacroPathName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentMacroPathName.md)  
[ISldWorks::GetMacroMethods Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMacroMethods.md)  
[ISldWorks::RunAttachedMacro Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunAttachedMacro.md)  
[ISldWorks::RecordLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RecordLine.md)  
[ISldWorks::RecordLineCSharp Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RecordLineCSharp.md)  
[ISldWorks::RecordLineVBnet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RecordLineVBnet.md)
